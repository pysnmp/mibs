#
# PySNMP MIB module APAMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAMI-MIB
# Produced by pysmi-1.1.8 at Fri Jan 13 14:36:17 2023
# On host fv-az358-896 platform Linux version 5.15.0-1030-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, iso, IpAddress, TimeTicks, Bits, Unsigned32, Gauge32, ObjectIdentity, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "iso", "IpAddress", "TimeTicks", "Bits", "Unsigned32", "Gauge32", "ObjectIdentity", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
apAMIModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 6))
apAMIModule.setRevisions(('2012-07-16 00:00', '2014-06-26 00:00',))
if mibBuilder.loadTexts: apAMIModule.setLastUpdated('201406260000Z')
if mibBuilder.loadTexts: apAMIModule.setOrganization('Oracle Communications')
apAMIMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 6, 1))
apAMISoapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1))
apAMISoapHttp = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAMISoapHttp.setStatus('current')
apAMISoapHttpPort = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAMISoapHttpPort.setStatus('current')
apAMISoapHttps = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAMISoapHttps.setStatus('current')
apAMISoapHttpsPort = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAMISoapHttpsPort.setStatus('current')
apAMIModuleConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 6, 2))
apAMIModuleGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 6, 2, 1))
apAMIMibObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 6, 2, 1, 1)).setObjects(("APAMI-MIB", "apAMISoapHttp"), ("APAMI-MIB", "apAMISoapHttpPort"), ("APAMI-MIB", "apAMISoapHttps"), ("APAMI-MIB", "apAMISoapHttpsPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAMIMibObjectsGroup = apAMIMibObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("APAMI-MIB", apAMISoapHttp=apAMISoapHttp, apAMIModule=apAMIModule, PYSNMP_MODULE_ID=apAMIModule, apAMIModuleConformance=apAMIModuleConformance, apAMIMIBObjects=apAMIMIBObjects, apAMISoapHttps=apAMISoapHttps, apAMISoapObjects=apAMISoapObjects, apAMIMibObjectsGroup=apAMIMibObjectsGroup, apAMIModuleGroups=apAMIModuleGroups, apAMISoapHttpPort=apAMISoapHttpPort, apAMISoapHttpsPort=apAMISoapHttpsPort)
