# Writing style for this repository

Applies to `docs/`, `README.md`, and any prose in the templates under `theme/`.

The reader is a network engineer with a problem: a device is returning an OID
they cannot name, a poller is failing to compile a module, a build needs a MIB
it does not have. They are scanning, not reading. Write for that.

## The rules

**Open by saying what the page is.** The first sentence states the page's
subject and scope. Do not begin with background, a scenario, or an example that
teaches SNMP.

> Before: SNMP names things in MIB modules. Without the module that defines
> it, an agent answering `1.3.6.1.2.1.2.2.1.8.1` tells you the value is `2`;
> with it, the same answer reads `IF-MIB::ifOperStatus.1 = down`. This is where
> the pysnmp organization publishes those modules.
>
> After: This site publishes the MIB modules that pysnmp and other SNMP tooling
> resolve against: 5,510 modules as ASN.1 and as JSON, with OID indexes.

**State the fact. Do not build to it.** No withheld conclusions, no sentence
that exists to set up the next one.

> Before: Three groups, and they need different things.
>
> After: The 194 modules fall into three groups.

**No aphorisms.** A sentence that would work on a slide is the wrong sentence.
If a claim is worth making, make it directly and support it.

> Before: A diff says what was changed and never what was wrong.
>
> After: Each patch records the defect it repairs, because the diff alone does
> not say why the change was needed.

**Keep the em dash for a genuine break in the sentence.** Do not use it to
attach a qualification, a reason, or a second thought. If the aside carries a
fact, it needs its own sentence. If it carries several, it needs a table.

**Do not give systems intentions.** Builds, sites and files do not want, know,
say, refuse, or do things quietly. Name the mechanism.

> Before: the deploy would publish the absence quietly
>
> After: the deploy publishes an empty tree and the job still succeeds

**No rhetorical questions, and no sentence fragments for emphasis.**

**No italics for verbal stress.** Use them only for a term being defined.

**Enumerable facts go in a table**, not in a sentence with commas.

**Procedures are numbered and imperative.** One action per step. Name the exact
menu, file, or command. Say what the result should be.

**Address the reader as "you". Do not use "we".** The repository is not a
person; write "this repository publishes", not "we publish".

**Name things exactly.** `index-v2.csv`, not "the newer index". Full paths, full
commands, exact option spellings.

**Give numbers with units and a date or version where they can change.**
"590 MB across 11,025 objects" beats "a large tree".

## What does not change

Reasoning stays. This repository documents why things are shaped the way they
are, and that is worth keeping — a reader who knows why `index.csv` is frozen
can predict what it will do next. The rule is that the reasoning is stated
plainly and in its own sentences, not compressed into an aside or sharpened
into an epigram.

Commit messages and pull request descriptions are not covered here. They argue
for a change to people reviewing it, which is a different job from documenting
a published artifact.

## Checking it

There is no linter for this. Before opening a pull request that touches prose,
re-read it against the list above, and in particular:

- Count the em dashes. More than one per 200 words means facts are hiding in
  asides.
- Read the first sentence of each page alone. It should say what the page is.
- Look for `nobody`, `somebody`, `quietly`, `says so`, `which is what`,
  `that is what`. Each is usually a sentence that should be rewritten.
