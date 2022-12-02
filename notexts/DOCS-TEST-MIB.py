#
# PySNMP MIB module DOCS-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/DOCS-TEST-MIB
# Produced by pysmi-1.1.8 at Fri Dec  2 16:40:05 2022
# On host fv-az545-99 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, iso, Gauge32, ObjectIdentity, enterprises, NotificationType, Unsigned32, Integer32, Counter32, IpAddress, Counter64, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "iso", "Gauge32", "ObjectIdentity", "enterprises", "NotificationType", "Unsigned32", "Integer32", "Counter32", "IpAddress", "Counter64", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DOCS-TEST-MIB", clabFunction=clabFunction, docsTestCapability=docsTestCapability, docsTestBasicCompliance=docsTestBasicCompliance, PYSNMP_MODULE_ID=docsTestMIB, docsTestStatus=docsTestStatus, clabProjPacketCable=clabProjPacketCable, docsTestSetupObjects=docsTestSetupObjects, docsTestConformance=docsTestConformance, cableLabs=cableLabs, clabProjCableHome=clabProjCableHome, docsTestGroups=docsTestGroups, docsTestBaseObjects=docsTestBaseObjects, clabFuncMib2=clabFuncMib2, docsTestType=docsTestType, docsTestMibObjects=docsTestMibObjects, clabProject=clabProject, docsTestData=docsTestData, clabFuncProprietary=clabFuncProprietary, docsTestMIB=docsTestMIB, docsTestEnable=docsTestEnable, docsTestCompliances=docsTestCompliances, clabProjDocsis=clabProjDocsis, clabProjOpenCable=clabProjOpenCable, docsTestGroup=docsTestGroup)
