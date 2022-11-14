from plover_speaker_id.lookup import spkr_table
from plover_speaker_id.utils import get_translation


def speaker_id_begin(ctx, arg):
  try:
    arg = int(arg)
  except ValueError:
    return ctx.copy_last_action()

  a = ctx.new_action()
  a.text = f"[Speaker {arg} ({spkr_table[arg]}) =>]"
  a.speaker_id = arg
  return a


def speaker_id_end(ctx, _):
  begin_action = None
  for action in ctx.iter_last_actions():
    if hasattr(action, "speaker_id"):
      begin_action = action
      break
  else:
    return ctx.copy_last_action()

  id = begin_action.speaker_id
  name = get_translation(ctx)
  spkr_table[id] = name
  spkr_table.save()
  a = ctx.new_action()
  a.prev_attach = True
  a.prev_replace = f"{begin_action.text} {name}"
  a.text = ""
  return a
