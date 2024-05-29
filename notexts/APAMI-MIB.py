#
# PySNMP MIB module APAMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAMI-MIB
# Produced by pysmi-1.1.12 at Wed May 29 08:14:13 2024
# On host fv-az698-992 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, IpAddress, MibIdentifier, Gauge32, Unsigned32, Counter64, NotificationType, Integer32, ModuleIdentity, iso, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "IpAddress", "MibIdentifier", "Gauge32", "Unsigned32", "Counter64", "NotificationType", "Integer32", "ModuleIdentity", "iso", "TimeTicks", "Bits")
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
mibBuilder.exportSymbols("APAMI-MIB", apAMIModule=apAMIModule, apAMISoapHttpPort=apAMISoapHttpPort, apAMISoapObjects=apAMISoapObjects, apAMIMibObjectsGroup=apAMIMibObjectsGroup, apAMISoapHttp=apAMISoapHttp, apAMISoapHttpsPort=apAMISoapHttpsPort, apAMIModuleConformance=apAMIModuleConformance, PYSNMP_MODULE_ID=apAMIModule, apAMIMIBObjects=apAMIMIBObjects, apAMISoapHttps=apAMISoapHttps, apAMIModuleGroups=apAMIModuleGroups)
