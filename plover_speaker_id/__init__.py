from plover_speaker_id.lookup import lookup_speaker_id
from plover_speaker_id.manage import speaker_id_begin, speaker_id_end
from plover_speaker_id.utils import new_action, new_inline, new_paragraph

question = new_paragraph(start="Q.")
question_double_space = new_paragraph(start="Q.", spaces=2)
answer = new_paragraph(start="A.")
answer_double_space = new_paragraph(start="A.", spaces=2)


inline_speaker_id = new_inline(text=lookup_speaker_id)


def _lookup_colloquy(id):
  return f"{lookup_speaker_id(id).upper()}:"


def _lookup_byline(id):
  return f"BY {lookup_speaker_id(id).upper()}:\nQ."


def _lookup_calif_byline(id):
  return f"{lookup_speaker_id(id).upper()}: Q."


colloquy = new_paragraph(start=_lookup_colloquy)
colloquy_double_space = new_paragraph(start=_lookup_colloquy, spaces=2)

byline = new_paragraph(start=_lookup_byline)
byline_double_space = new_paragraph(start=_lookup_byline, spaces=2)

calif_byline = new_paragraph(start=_lookup_calif_byline)
calif_byline_double_space = new_paragraph(start=_lookup_calif_byline, spaces=2)


def _lookup_double_arrow(id):
  return f">> {lookup_speaker_id(id).upper()}:"


caption = new_paragraph(start=">>>")
caption_double_space = new_paragraph(start=">>>", spaces=2)


caption_speaker = new_paragraph(start=_lookup_double_arrow)
caption_speaker_double_space = new_paragraph(
  start=_lookup_double_arrow, spaces=2
)
