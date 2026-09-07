#
# PySNMP MIB module URI-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source URI-TC-MIB
# Source digest sha256:fc808797a60dc5da78d578a8b7a17ea5ec64a0230645a5f924c1cc478290951a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
uriTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 164))
uriTcMIB.setRevisions(('2007-09-10 00:00',))
if mibBuilder.loadTexts: uriTcMIB.setLastUpdated('2007-09-10 00:00')
if mibBuilder.loadTexts: uriTcMIB.setOrganization('IETF Operations and Management (OPS) Area')
class Uri(TextualConvention, OctetString):
    reference = 'RFC 3986 STD 66 and RFC 3305'
    status = 'current'
    displayHint = '1a'

class Uri255(TextualConvention, OctetString):
    reference = 'RFC 3986 STD 66 and RFC 3305'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Uri1024(TextualConvention, OctetString):
    reference = 'RFC 3986 STD 66 and RFC 3305'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

mibBuilder.exportSymbols("URI-TC-MIB", PYSNMP_MODULE_ID=uriTcMIB, Uri1024=Uri1024, Uri255=Uri255, Uri=Uri, uriTcMIB=uriTcMIB)
