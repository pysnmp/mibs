#
# PySNMP MIB module BASIS-ONLINE-DIAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source BASIS-ONLINE-DIAG-MIB
# Source digest sha256:34235012a13c73c28793c5b7b03bf37dd78b1fcc15f6539ada1db302031a19b7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
axisDiagnostics, = mibBuilder.importSymbols("BASIS-MIB", "axisDiagnostics")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
basisOnlineDiagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 80))
basisOnlineDiagMIB.setRevisions(('2003-06-11 00:00',))
if mibBuilder.loadTexts: basisOnlineDiagMIB.setLastUpdated('2003-06-11 00:00')
if mibBuilder.loadTexts: basisOnlineDiagMIB.setOrganization('Cisco Systems, Inc.')
onlineDiagnostics = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 6, 3))
diagType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("post", 1), ("onlinediag", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagType.setStatus('current')
diagResult = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("passed", 1), ("failed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagResult.setStatus('current')
diagTestId = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagTestId.setStatus('current')
boDiagMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2))
boDiagMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 1))
boDiagMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 2))
boDiagCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 1, 1)).setObjects(("BASIS-ONLINE-DIAG-MIB", "boDiagGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    boDiagCompliance = boDiagCompliance.setStatus('current')
boDiagGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 2, 1)).setObjects(("BASIS-ONLINE-DIAG-MIB", "diagType"), ("BASIS-ONLINE-DIAG-MIB", "diagResult"), ("BASIS-ONLINE-DIAG-MIB", "diagTestId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    boDiagGroup = boDiagGroup.setStatus('current')
mibBuilder.exportSymbols("BASIS-ONLINE-DIAG-MIB", PYSNMP_MODULE_ID=basisOnlineDiagMIB, basisOnlineDiagMIB=basisOnlineDiagMIB, boDiagCompliance=boDiagCompliance, boDiagGroup=boDiagGroup, boDiagMIBCompliances=boDiagMIBCompliances, boDiagMIBConformance=boDiagMIBConformance, boDiagMIBGroups=boDiagMIBGroups, diagResult=diagResult, diagTestId=diagTestId, diagType=diagType, onlineDiagnostics=onlineDiagnostics)
