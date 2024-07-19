#
# PySNMP MIB module STORMSHIELD-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-SERVICES-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 09:49:55 2024
# On host fv-az1778-45 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, iso, ObjectIdentity, Unsigned32, Bits, NotificationType, IpAddress, Counter32, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "ObjectIdentity", "Unsigned32", "Bits", "NotificationType", "IpAddress", "Counter32", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Integer32")
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
mibBuilder.exportSymbols("STORMSHIELD-SERVICES-MIB", PYSNMP_MODULE_ID=snsServices, snsServicesName=snsServicesName, snsServicesUptime=snsServicesUptime, snsServicesTable=snsServicesTable, snsServicesState=snsServicesState, snsServicesEntry=snsServicesEntry, snsServices=snsServices, snsServicesIndex=snsServicesIndex)
