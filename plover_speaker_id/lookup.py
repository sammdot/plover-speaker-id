DEFAULT_SPEAKERS = {
  1: "Mr. Stphao",
  2: "Ms. Skwrao",
  3: "Mr. Eufplt",
  4: "Ms. Eurbgs",
  300: "the Witness",
  301: "the Court",
  302: "the Videographer",
  303: "the Court Reporter",
  304: "the Clerk",
  305: "the Bailiff",
}


class SpeakerTable:
  def __init__(self):
    # TODO: load speaker IDs from external file in Plover's config directory
    self._speakers = DEFAULT_SPEAKERS

  def __getitem__(self, id: int) -> str:
    return self._speakers.get(id, f"[Speaker {id}]")

  def __setitem__(self, id: int, name: str):
    self._speakers[id] = name


spkr_table = SpeakerTable()


def lookup_speaker_id(id: int) -> str:
  try:
    id = int(id)
  except ValueError:
    pass
  return spkr_table[id]
