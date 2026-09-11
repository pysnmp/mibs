# Using the distribution

Two things people do with it, and the one wrinkle between them.

## Resolving a name

The everyday reason to care. `IF-MIB` is not one of the modules pysnmp ships,
so naming an object in it needs pysmi and a source to read from:

```python
from pysnmp.smi import builder, compiler, rfc1902, view

mibBuilder = builder.MibBuilder()
compiler.addMibCompiler(
    mibBuilder, sources=["https://pysnmp.github.io/mibs/asn1/@mib@"]
)
mibView = view.MibViewController(mibBuilder)

identity = rfc1902.ObjectIdentity("IF-MIB", "ifInOctets", 1)
identity.resolveWithMib(mibView)

print(identity.getOid())
```

```text
1.3.6.1.2.1.2.2.1.10.1
```

The `@mib@` in the source is a placeholder pysmi substitutes with the module
name it wants; it is not a URL you would open. The first resolution compiles
`IF-MIB`; later ones read the compiled copy. Hand the same `ObjectIdentity` to
`getCmd` or `nextCmd` and you are polling by name.

## Translating a trap

A notification arrives as bare numbers. Turning it into something a human or a
log pipeline can read is the same machinery in reverse, with one wrinkle worth
knowing: **an OID carries no hint of which module defines it**, so the modules
you care about have to be loaded before the lookup can succeed. Resolving
against an empty builder raises `SmiError: ... (MIB not loaded?)`.

```python
from pysnmp.smi import builder, compiler, rfc1902, view

mibBuilder = builder.MibBuilder()
compiler.addMibCompiler(
    mibBuilder, sources=["https://pysnmp.github.io/mibs/asn1/@mib@"]
)
# Load what this receiver expects to see. Without this the reverse lookup
# has nothing to search.
mibBuilder.loadModules("SNMPv2-MIB", "IF-MIB")
mibView = view.MibViewController(mibBuilder)

# What a linkDown trap actually carries on the wire.
varBinds = [
    ("1.3.6.1.6.3.1.1.4.1.0", "1.3.6.1.6.3.1.1.5.3"),
    ("1.3.6.1.2.1.2.2.1.1.1", 1),
    ("1.3.6.1.2.1.2.2.1.8.1", 2),
]

for oid, value in varBinds:
    varBind = rfc1902.ObjectType(rfc1902.ObjectIdentity(oid), value)
    varBind.resolveWithMib(mibView)
    print(varBind.prettyPrint())
```

```text
SNMPv2-MIB::snmpTrapOID.0 = IF-MIB::linkDown
IF-MIB::ifIndex.1 = 1
IF-MIB::ifOperStatus.1 = down
```

Note the last line. `2` became `down` because the textual convention in
`IF-MIB` says so — this distribution gives you the enumeration labels, not just
the names.

Where a receiver cannot know in advance which modules a trap will name,
[`core.db`](corpora.md#the-corpus-database) answers the other way round: one
indexed query per arc, from an OID to the module, the name, the syntax and the
access level, with no compile on the trap path.

## Pointing pysmi somewhere else

The source is a list, and the first hit wins, so a local directory in front of
the published tree is how you override a module or work offline:

```python
compiler.addMibCompiler(
    mibBuilder,
    sources=[
        "/usr/share/snmp/mibs",
        "https://pysnmp.github.io/mibs/asn1/@mib@",
    ],
)
```

The same list is what `mibdump` takes on the command line. Most vendor MIBs are
not public, so this is the normal arrangement rather than the exception.

An unpacked `mibs-asn1.zip` or a mounted `corpus-compact` image is a local
directory like any other — see [channels](channels.md).

```{warning}
A MIB module compiled by pysmi becomes Python that pysnmp imports. Treat an
ASN.1 MIB source the way you would treat any other code you are about to run,
and compile from somewhere you trust.
```
