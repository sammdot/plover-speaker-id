# Plover Speaker ID

A Plover plugin for managing speaker identification and question-and-answer
designations. Define your speaker IDs inline and use them right away.

## Speaker Numbers

Speaker numbers are somewhat arbitrary, and you can have as many items defined
in your dictionary as you need. The predefined speaker IDs range from 1 to 4
for regular speakers, and 300 upwards for some special roles.

| Num | Name                 |
| --: | -------------------- |
|   1 | `Mr. Stphao`         |
|   2 | `Ms. Skwrao`         |
|   3 | `Mr. Eufplt`         |
|   4 | `Ms. Eurbgs`         |
| 300 | `the Witness`        |
| 301 | `the Court`          |
| 302 | `the Videographer`   |
| 303 | `the Court Reporter` |
| 304 | `the Clerk`          |
| 305 | `the Bailiff`        |

These are by no means the only speaker IDs available. Feel free to redefine the
speaker names, or add more to fit your use case.

## Writing Designations

To actually write designations, you can define outlines to translate to special
operators in your personal dictionaries.

_Note: The outlines used below are merely examples from my own usage; feel free
to use outlines that match your own theory or personal dictionary._

### Question and Answer

Questions can be defined with the `:question` meta, and answers with `:answer`:

```json
"STKPWHR": "{:question}"
"-FRPBLGTS": "{:answer}"
```

Both of these start a new line with either `Q.` or `A.`. To start a paragraph
double-spaced, use the `:question_dsp`/`:Q` or `:answer_dsp`/`:A` metas.

### Speaker Identification (Court Reporting)

To start a paragraph of colloquy, use the `:colloquy` meta, and provide
a speaker number:

```json
"STPHAO": "{:colloquy:1}"
"SKWRAO": "{:colloquy:2}"
```

It starts a new line with the speaker's name _in all upper case_ followed by
a colon, for example `MR. SNOO:`. To start double-spaced, use
`:colloquy_dsp`/`:coll`.

For bylines, use the `:byline` meta, and provide a speaker number:

```json
"STPHAO/STKPWHR": "{:byline:1}"
"SKWRAO/STKPWHR": "{:byline:2}"
```

This outputs a byline of the form `BY <speaker>:`, followed by a `Q.` on the
next line. To start double-spaced, use `:byline_dsp`/`:by`.

California-style bylines have the initial `Q.` on the same line as the speaker
name. To use this style, prefix the meta names with `ca_`: `:ca_byline`,
`:ca_byline_dsp`/`:ca_by`.

### Speaker Identification (Captioning)

To start a paragraph by a certain speaker, use the `:cap_speaker` meta, and
provide the speaker number:

```json
"STPHAO": "{:cap_speaker:1}"
"SKWRAO": "{:cap_speaker:2}"
```

This starts a new line with two arrows `>>`, then the speaker's name, then
a colon. To start double-spaced, use `:cap_speaker_dsp`/`:capspkr`.

To start a paragraph without a named speaker, use `:caption` and don't provide
a number. For double spacing, use `:caption_dsp`/`:cap`.

```json
"EUFPLT": "{:caption}"
```

### Inline Speaker Names

To write a speaker's name inline, use the `:spkr_inline` meta with a speaker
number:

```json
"EUFPLT": "{:spkr_inline:3}"
```

## Speaker Management

Before editing speaker names, you'll need to define some dictionary entries.

First, define an entry in your personal dictionary using
`:speaker_id_set`/`:spkrid_set` for setting the name for that specific speaker
number. I like to use `SKPREUD` ("skpr-id") followed by the speaker's outline:

```json
"SKPREUD/STPHAO": "{:spkrid_set:1}"
"SKPREUD/SKWRAO": "{:spkrid_set:2}"
```

And also have a single outline for ending a speaker definition, using
`:speaker_id_end`/`:spkrid_end`. I like to use `SKPREUDZ` ("skpr-idz").

```json
"SKPREUDZ": "{:spkrid_end}"
```

To define a speaker name, write your outline for setting the name. You should
get a prompt that mentions the speaker ID and current name:

```
+------------------------+
|                        |
| S KP  R   EU        D  |
| S K W RAO              | [Speaker 2 (Ms. Skwrao) =>]
|                        |
```

Then, write the new name:

```
|                        |
|    P H               Z | Ms.
|   K  H A      PB       | Chan
|                        |
```

Lastly, write the outline to end. This deletes the prompt and the name, and
now the name is ready to use.

```
|                        |
| S KP  R   EU        DZ |
|                        |
+------------------------+
```
