from plover.oslayer.config import CONFIG_DIR
import json
import pathlib
spkr_dict_path = pathlib.Path(CONFIG_DIR) / "spkr.json"

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
    self._speakers = DEFAULT_SPEAKERS
    if not spkr_dict_path.exists():
        self.save()
    else:
        with open(spkr_dict_path, "r") as f:
            self._speakers = json.loads(f.read(), object_hook=lambda d: {int(k) if k.lstrip('-').isdigit() else k: v for k, v in d.items()})

  def __getitem__(self, id: int) -> str:
    return self._speakers.get(id, f"[Speaker {id}]")

  def __setitem__(self, id: int, name: str):
    self._speakers[id] = name

  def save(self):
    with open(spkr_dict_path, "w") as f:
      json.dump(self._speakers, f)    

spkr_table = SpeakerTable()


def lookup_speaker_id(id: int) -> str:
  try:
    id = int(id)
  except ValueError:
    pass
  return spkr_table[id]
