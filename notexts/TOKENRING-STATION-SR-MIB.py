#
# PySNMP MIB module TOKENRING-STATION-SR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source TOKENRING-STATION-SR-MIB
# Source digest sha256:87053e690b155db41906b535b10d10e9b27827368dbd7f7bb0fb6ede269d353b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "mib-2")
DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
dot5SrMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 42))
if mibBuilder.loadTexts: dot5SrMIB.setLastUpdated('1994-12-16 10:00')
if mibBuilder.loadTexts: dot5SrMIB.setOrganization('IETF Interfaces MIB Working Group')
dot5SrMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 1))
class SourceRoute(TextualConvention, OctetString):
    reference = 'Annex C of ISO/IEC 10038: 1993, [ANSI/IEEE Std 802.1D, 1993]'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

dot5SrRouteTable = MibTable((1, 3, 6, 1, 2, 1, 42, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dot5SrRouteTable.setStatus('current')
dot5SrRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 42, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TOKENRING-STATION-SR-MIB", "dot5SrRouteDestination"))
if mibBuilder.loadTexts: dot5SrRouteEntry.setStatus('current')
dot5SrRouteDestination = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 2), MacAddress()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dot5SrRouteDestination.setStatus('current')
dot5SrRouteControl = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot5SrRouteControl.setStatus('current')
dot5SrRouteDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 4), SourceRoute()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot5SrRouteDescr.setStatus('current')
dot5SrRouteStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot5SrRouteStatus.setStatus('current')
dot5SrConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 2))
dot5SrGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 2, 1))
dot5SrCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 2, 2))
dot5SrCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 42, 2, 2, 1)).setObjects(("TOKENRING-STATION-SR-MIB", "dot5SrRouteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot5SrCompliance = dot5SrCompliance.setStatus('current')
dot5SrRouteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 42, 2, 1, 1)).setObjects(("TOKENRING-STATION-SR-MIB", "dot5SrRouteControl"), ("TOKENRING-STATION-SR-MIB", "dot5SrRouteDescr"), ("TOKENRING-STATION-SR-MIB", "dot5SrRouteStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot5SrRouteGroup = dot5SrRouteGroup.setStatus('current')
mibBuilder.exportSymbols("TOKENRING-STATION-SR-MIB", PYSNMP_MODULE_ID=dot5SrMIB, SourceRoute=SourceRoute, dot5SrCompliance=dot5SrCompliance, dot5SrCompliances=dot5SrCompliances, dot5SrConformance=dot5SrConformance, dot5SrGroups=dot5SrGroups, dot5SrMIB=dot5SrMIB, dot5SrMIBObjects=dot5SrMIBObjects, dot5SrRouteControl=dot5SrRouteControl, dot5SrRouteDescr=dot5SrRouteDescr, dot5SrRouteDestination=dot5SrRouteDestination, dot5SrRouteEntry=dot5SrRouteEntry, dot5SrRouteGroup=dot5SrRouteGroup, dot5SrRouteStatus=dot5SrRouteStatus, dot5SrRouteTable=dot5SrRouteTable)
