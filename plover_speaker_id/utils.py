from plover.formatting import Case


def new_action(*, text_fn=None, text=None, cap=False):
  def _action(ctx, arg):
    a = ctx.new_action()
    if text:
      a.text = text
    elif text_fn:
      a.text = text_fn(arg)
    if upper:
      a.next_case
    return a

  return _action


def new_paragraph(*, start, spaces=1):
  def _action(ctx, arg):
    nonlocal start
    if callable(start):
      start_text = start(arg)
    else:
      start_text = start

    a = ctx.new_action()
    a.prev_attach = True
    a.text = f"\n{start_text}".replace("\n", "\n" * spaces)
    a.next_case = Case.CAP_FIRST_WORD
    return a

  return _action


def new_inline(*, text):
  def _action(ctx, arg):
    nonlocal text
    if callable(text):
      start_text = text(arg)
    else:
      start_text = text

    a = ctx.new_action()
    a.text = start_text
    return a

  return _action


# Modified from Plover's plover.formatting.RetroFormatter.iter_last_fragments
def get_translation(ctx):
  replace = 0
  next_action = None
  current_fragment = ""
  for action in ctx.iter_last_actions():
    if hasattr(action, "speaker_id"):
      break
    part = "" if action.text is None else action.text
    if (
      next_action is not None
      and next_action.text is not None
      and not next_action.prev_attach
    ):
      part += next_action.space_char
    if replace:
      # Ignore replaced content.
      if len(part) > replace:
        part = part[:-replace]
        replace = 0
      else:
        replace -= len(part)
        part = ""
    current_fragment = part + current_fragment
    replace += len(action.prev_replace)
    next_action = action

  return current_fragment
