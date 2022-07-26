#
# PySNMP MIB module STORMSHIELD-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-SERVICES-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 16:26:05 2022
# On host fv-az377-45 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Unsigned32, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, Gauge32, Integer32, Counter32, ModuleIdentity, iso, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "Gauge32", "Integer32", "Counter32", "ModuleIdentity", "iso", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsServices = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 7))
snsServices.setRevisions(('2017-02-20 00:00',))
if mibBuilder.loadTexts: snsServices.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsServices.setOrganization('Stormshield')
snsServicesTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 7, 1), )
if mibBuilder.loadTexts: snsServicesTable.setStatus('current')
snsServicesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 7, 1, 1), ).setIndexNames((0, "STORMSHIELD-SERVICES-MIB", "snsServicesIndex"))
if mibBuilder.loadTexts: snsServicesEntry.setStatus('current')
snsServicesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsServicesIndex.setStatus('current')
snsServicesName = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 7, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsServicesName.setStatus('current')
snsServicesState = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 7, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsServicesState.setStatus('current')
snsServicesUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 7, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsServicesUptime.setStatus('current')
mibBuilder.exportSymbols("STORMSHIELD-SERVICES-MIB", PYSNMP_MODULE_ID=snsServices, snsServices=snsServices, snsServicesUptime=snsServicesUptime, snsServicesEntry=snsServicesEntry, snsServicesTable=snsServicesTable, snsServicesIndex=snsServicesIndex, snsServicesName=snsServicesName, snsServicesState=snsServicesState)
