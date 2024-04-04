#
# PySNMP MIB module STORMSHIELD-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-SERVICES-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:23:32 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, Gauge32, MibIdentifier, ObjectIdentity, NotificationType, Counter32, iso, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "Gauge32", "MibIdentifier", "ObjectIdentity", "NotificationType", "Counter32", "iso", "TimeTicks", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("STORMSHIELD-SERVICES-MIB", PYSNMP_MODULE_ID=snsServices, snsServicesEntry=snsServicesEntry, snsServicesName=snsServicesName, snsServicesUptime=snsServicesUptime, snsServicesState=snsServicesState, snsServices=snsServices, snsServicesTable=snsServicesTable, snsServicesIndex=snsServicesIndex)
