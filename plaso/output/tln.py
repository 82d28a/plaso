# -*- coding: utf-8 -*-
"""Output module for the TLN format.

For documentation on the TLN format see:
https://forensicswiki.xyz/wiki/index.php?title=TLN
"""

from __future__ import unicode_literals

from dfdatetime import posix_time as dfdatetime_posix_time

from plaso.lib import errors
from plaso.lib import timelib
from plaso.output import formatting_helper
from plaso.output import manager
from plaso.output import shared_dsv


class TLNFieldFormattingHelper(formatting_helper.FieldFormattingHelper):
  """TLN output module field formatting helper."""

  _DESCRIPTION_FIELD_DELIMITER = ';'

  _FIELD_FORMAT_CALLBACKS = {
      'description': '_FormatDescription',
      'host': '_FormatHostname',
      'inode': '_FormatInode',
      'notes': '_FormatNotes',
      'source': '_FormatSourceShort',
      'time': '_FormatTimestamp',
      'tz': '_FormatTimeZone',
      'user': '_FormatUsername',
  }

  # The field format callback methods require specific arguments hence
  # the check for unused arguments is disabled here.
  # pylint: disable=unused-argument

  def _FormatDescription(self, event, event_data, event_data_stream):
    """Formats a description field.

    Args:
      event (EventObject): event.
      event_data (EventData): event data.
      event_data_stream (EventDataStream): event data stream.

    Returns:
      str: description field.

    Raises:
      NoFormatterFound: If no event formatter can be found to match the data
          type in the event data.
    """
    date_time_string = timelib.Timestamp.CopyToIsoFormat(
        event.timestamp, timezone=self._output_mediator.timezone)
    timestamp_description = event.timestamp_desc or 'UNKNOWN'

    message, _ = self._output_mediator.GetFormattedMessages(event_data)
    if message is None:
      data_type = getattr(event_data, 'data_type', 'UNKNOWN')
      raise errors.NoFormatterFound(
          'Unable to find event formatter for: {0:s}.'.format(data_type))

    return '{0:s}; {1:s}; {2:s}'.format(
        date_time_string, timestamp_description,
        message.replace(self._DESCRIPTION_FIELD_DELIMITER, ' '))

  def _FormatNotes(self, event, event_data, event_data_stream):
    """Formats a notes field.

    Args:
      event (EventObject): event.
      event_data (EventData): event data.
      event_data_stream (EventDataStream): event data stream.

     Returns:
       str: formatted notes field.
    """
    inode = self._FormatInode(event, event_data, event_data_stream)

    notes = getattr(event_data, 'notes', '')
    if not notes:
      display_name = getattr(event_data, 'display_name', '')
      notes = 'File: {0:s} inode: {1!s}'.format(display_name, inode)

    return notes

  def _FormatTimestamp(self, event, event_data, event_data_stream):
    """Formats a timestamp.

    Args:
      event (EventObject): event.
      event_data (EventData): event data.
      event_data_stream (EventDataStream): event data stream.

    Returns:
      str: timestamp.
    """
    # TODO: preserve dfdatetime as an object.
    date_time = dfdatetime_posix_time.PosixTimeInMicroseconds(
        timestamp=event.timestamp)
    posix_timestamp = date_time.CopyToPosixTimestamp()
    if not posix_timestamp:
      posix_timestamp = 0

    return '{0:d}'.format(posix_timestamp)


class TLNOutputModule(shared_dsv.DSVOutputModule):
  """Output module for the TLN format.

  TLN defines 5 | separated fields, namely:
  * Time - 32-bit POSIX (or Unix) epoch timestamp.
  * Source - The name of the parser or plugin that produced the event.
  * Host - The source host system.
  * User - The user associated with the data.
  * Description - Message string describing the data.
  """
  NAME = 'tln'
  DESCRIPTION = 'TLN 5 field | delimited output.'

  _FIELD_NAMES = ['time', 'source', 'host', 'user', 'description']

  _HEADER = 'Time|Source|Host|User|Description'

  def __init__(self, output_mediator):
    """Initializes a TLN output module.

    Args:
      output_mediator (OutputMediator): mediates interactions between output
          modules and other components, such as storage and dfvfs.
    """
    formatting_helper_object = TLNFieldFormattingHelper(output_mediator)
    super(TLNOutputModule, self).__init__(
        output_mediator, formatting_helper_object, self._FIELD_NAMES,
        delimiter='|', header=self._HEADER)


class L2TTLNOutputModule(shared_dsv.DSVOutputModule):
  """Output module for the log2timeline extended variant of the TLN format.

  l2tTLN is an extended variant of TLN introduced log2timeline 0.65.

  l2tTLN extends basic TLN to 7 | separated fields, namely:
  * Time - 32-bit POSIX (or Unix) epoch timestamp.
  * Source - The name of the parser or plugin that produced the event.
  * Host - The source host system.
  * User - The user associated with the data.
  * Description - Message string describing the data.
  * TZ - L2T 0.65 field. Timezone of the event.
  * Notes - L2T 0.65 field. Optional notes field or filename and inode.
  """
  NAME = 'l2ttln'
  DESCRIPTION = 'Extended TLN 7 field | delimited output.'

  _FIELD_NAMES = [
      'time', 'source', 'host', 'user', 'description', 'tz', 'notes']

  _HEADER = 'Time|Source|Host|User|Description|TZ|Notes'

  def __init__(self, output_mediator):
    """Initializes a log2timeline extended variant of TLN output module.

    Args:
      output_mediator (OutputMediator): mediates interactions between output
          modules and other components, such as storage and dfvfs.
    """
    formatting_helper_object = TLNFieldFormattingHelper(output_mediator)
    super(L2TTLNOutputModule, self).__init__(
        output_mediator, formatting_helper_object, self._FIELD_NAMES,
        delimiter='|', header=self._HEADER)


manager.OutputManager.RegisterOutputs([L2TTLNOutputModule, TLNOutputModule])
