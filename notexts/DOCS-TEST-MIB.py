#
# PySNMP MIB module DOCS-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/DOCS-TEST-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 10:08:44 2023
# On host fv-az732-878 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, Integer32, enterprises, Bits, TimeTicks, Gauge32, ObjectIdentity, Unsigned32, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "Integer32", "enterprises", "Bits", "TimeTicks", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "ModuleIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
cableLabs = MibIdentifier((1, 3, 6, 1, 4, 1, 4491))
clabFunction = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 1))
clabFuncMib2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 1, 1))
clabFuncProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 1, 2))
clabProject = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2))
clabProjDocsis = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1))
clabProjPacketCable = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2))
clabProjOpenCable = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 3))
clabProjCableHome = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4))
docsTestMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12))
if mibBuilder.loadTexts: docsTestMIB.setLastUpdated('0203150000Z')
if mibBuilder.loadTexts: docsTestMIB.setOrganization('DOCSIS 2.0 ATP Working Group')
docsTestMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1))
docsTestBaseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 1))
docsTestSetupObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 2))
docsTestCapability = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsTestCapability.setStatus('current')
docsTestStatus = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsTestStatus.setStatus('current')
docsTestType = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsTestType.setStatus('current')
docsTestData = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 2, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsTestData.setStatus('current')
docsTestEnable = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 2, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsTestEnable.setStatus('current')
docsTestConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2))
docsTestCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2, 1))
docsTestGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2, 2))
docsTestBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2, 1, 1)).setObjects(("DOCS-TEST-MIB", "docsTestGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsTestBasicCompliance = docsTestBasicCompliance.setStatus('current')
docsTestGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2, 2, 1)).setObjects(("DOCS-TEST-MIB", "docsTestCapability"), ("DOCS-TEST-MIB", "docsTestStatus"), ("DOCS-TEST-MIB", "docsTestType"), ("DOCS-TEST-MIB", "docsTestData"), ("DOCS-TEST-MIB", "docsTestEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsTestGroup = docsTestGroup.setStatus('current')
mibBuilder.exportSymbols("DOCS-TEST-MIB", clabProjPacketCable=clabProjPacketCable, clabProjOpenCable=clabProjOpenCable, clabProjDocsis=clabProjDocsis, docsTestType=docsTestType, clabProjCableHome=clabProjCableHome, clabFuncMib2=clabFuncMib2, docsTestStatus=docsTestStatus, docsTestSetupObjects=docsTestSetupObjects, docsTestMibObjects=docsTestMibObjects, docsTestCompliances=docsTestCompliances, PYSNMP_MODULE_ID=docsTestMIB, docsTestGroups=docsTestGroups, clabProject=clabProject, cableLabs=cableLabs, clabFuncProprietary=clabFuncProprietary, docsTestBasicCompliance=docsTestBasicCompliance, docsTestConformance=docsTestConformance, docsTestData=docsTestData, clabFunction=clabFunction, docsTestMIB=docsTestMIB, docsTestGroup=docsTestGroup, docsTestCapability=docsTestCapability, docsTestEnable=docsTestEnable, docsTestBaseObjects=docsTestBaseObjects)
