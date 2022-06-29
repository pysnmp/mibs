#
# PySNMP MIB module DOCS-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/DOCS-TEST-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:03:26 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, Integer32, TimeTicks, NotificationType, Gauge32, Bits, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, ObjectIdentity, MibIdentifier, Counter64, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "TimeTicks", "NotificationType", "Gauge32", "Bits", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Counter64", "IpAddress", "Counter32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("DOCS-TEST-MIB", clabFuncProprietary=clabFuncProprietary, docsTestMIB=docsTestMIB, clabProject=clabProject, clabProjOpenCable=clabProjOpenCable, docsTestStatus=docsTestStatus, docsTestData=docsTestData, docsTestBaseObjects=docsTestBaseObjects, clabProjCableHome=clabProjCableHome, docsTestBasicCompliance=docsTestBasicCompliance, docsTestConformance=docsTestConformance, clabFuncMib2=clabFuncMib2, clabFunction=clabFunction, cableLabs=cableLabs, clabProjDocsis=clabProjDocsis, docsTestMibObjects=docsTestMibObjects, docsTestEnable=docsTestEnable, clabProjPacketCable=clabProjPacketCable, docsTestType=docsTestType, PYSNMP_MODULE_ID=docsTestMIB, docsTestCompliances=docsTestCompliances, docsTestSetupObjects=docsTestSetupObjects, docsTestGroups=docsTestGroups, docsTestGroup=docsTestGroup, docsTestCapability=docsTestCapability)
