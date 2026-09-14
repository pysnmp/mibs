# Using the distribution

This page covers the two common operations: resolving a name to an OID, and
translating a received OID back to a name. It ends with how to point pysmi at a
local directory instead of, or ahead of, the published tree.

## Resolving a name

`IF-MIB` is not among the modules pysnmp ships, so naming an object in it
requires pysmi and a source to read from:

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

`@mib@` is a placeholder that pysmi substitutes with the module name it
needs. It is not a URL you open in a browser.

The first resolution compiles `IF-MIB`. Later ones read the compiled copy. Pass
the same `ObjectIdentity` to `getCmd` or `nextCmd` to poll by name.

## Translating a trap

A notification arrives as bare numbers. Translating it uses the same machinery
in reverse, with one requirement.

An OID carries no indication of which module defines it. Load the modules the
receiver expects before the lookup. Resolving against an empty builder raises
`SmiError: ... (MIB not loaded?)`.

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

In the last line, `2` is rendered as `down` by the textual convention in
`IF-MIB`. The distribution carries the enumeration labels, not only the object
names.

Where a receiver cannot know in advance which modules a trap will name,
[`core.db`](corpora.md#the-corpus-database) resolves in the other direction:
one indexed query per arc returns the module, the name, the syntax and the
access level, with no compile on the trap path.

## Pointing pysmi somewhere else

The source list is ordered and the first hit wins. Put a local directory ahead
of the published tree to override a module or to compile without network
access:

```python
compiler.addMibCompiler(
    mibBuilder,
    sources=[
        "/usr/share/snmp/mibs",
        "https://pysnmp.github.io/mibs/asn1/@mib@",
    ],
)
```

`mibdump` takes the same list on the command line. Most vendor MIBs are not
published, so a local directory ahead of the tree is the usual arrangement.

An unpacked `mibs-asn1.zip` or a mounted `corpus-compact` image is a local
directory like any other. See [channels](channels.md).

```{warning}
A MIB module compiled by pysmi becomes Python that pysnmp executes. Treat an
ASN.1 MIB source as code you are about to run, and compile only from a source
you trust.
```
