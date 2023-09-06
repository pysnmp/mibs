#
# PySNMP MIB module APAMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAMI-MIB
# Produced by pysmi-1.1.8 at Wed Sep  6 13:55:42 2023
# On host fv-az254-698 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.12 (main, Jun  7 2023, 13:43:11) [GCC 11.3.0]
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Integer32, iso, ObjectIdentity, MibIdentifier, NotificationType, ModuleIdentity, Bits, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Integer32", "iso", "ObjectIdentity", "MibIdentifier", "NotificationType", "ModuleIdentity", "Bits", "Gauge32", "IpAddress")
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
mibBuilder.exportSymbols("APAMI-MIB", apAMISoapHttps=apAMISoapHttps, apAMIMibObjectsGroup=apAMIMibObjectsGroup, PYSNMP_MODULE_ID=apAMIModule, apAMISoapHttpPort=apAMISoapHttpPort, apAMIModule=apAMIModule, apAMIMIBObjects=apAMIMIBObjects, apAMISoapHttp=apAMISoapHttp, apAMIModuleConformance=apAMIModuleConformance, apAMISoapObjects=apAMISoapObjects, apAMISoapHttpsPort=apAMISoapHttpsPort, apAMIModuleGroups=apAMIModuleGroups)
