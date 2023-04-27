#
# PySNMP MIB module DOCS-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/DOCS-TEST-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 12:05:33 2023
# On host fv-az566-662 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, Bits, Unsigned32, ModuleIdentity, Integer32, NotificationType, IpAddress, MibIdentifier, TimeTicks, enterprises, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "Bits", "Unsigned32", "ModuleIdentity", "Integer32", "NotificationType", "IpAddress", "MibIdentifier", "TimeTicks", "enterprises", "Counter32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
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
mibBuilder.exportSymbols("DOCS-TEST-MIB", PYSNMP_MODULE_ID=docsTestMIB, clabFuncProprietary=clabFuncProprietary, clabProjCableHome=clabProjCableHome, clabProjOpenCable=clabProjOpenCable, clabFuncMib2=clabFuncMib2, docsTestData=docsTestData, docsTestMIB=docsTestMIB, docsTestCompliances=docsTestCompliances, docsTestGroup=docsTestGroup, clabProjPacketCable=clabProjPacketCable, clabProjDocsis=clabProjDocsis, docsTestStatus=docsTestStatus, docsTestConformance=docsTestConformance, docsTestEnable=docsTestEnable, docsTestCapability=docsTestCapability, docsTestBasicCompliance=docsTestBasicCompliance, docsTestSetupObjects=docsTestSetupObjects, docsTestGroups=docsTestGroups, clabFunction=clabFunction, docsTestBaseObjects=docsTestBaseObjects, cableLabs=cableLabs, clabProject=clabProject, docsTestMibObjects=docsTestMibObjects, docsTestType=docsTestType)
