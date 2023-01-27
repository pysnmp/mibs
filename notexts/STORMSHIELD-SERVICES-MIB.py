#
# PySNMP MIB module STORMSHIELD-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-SERVICES-MIB
# Produced by pysmi-1.1.8 at Fri Jan 27 14:14:09 2023
# On host fv-az417-962 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, iso, Unsigned32, IpAddress, MibIdentifier, ObjectIdentity, Gauge32, NotificationType, Integer32, TimeTicks, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "iso", "Unsigned32", "IpAddress", "MibIdentifier", "ObjectIdentity", "Gauge32", "NotificationType", "Integer32", "TimeTicks", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
mibBuilder.exportSymbols("STORMSHIELD-SERVICES-MIB", snsServicesTable=snsServicesTable, snsServicesState=snsServicesState, snsServicesUptime=snsServicesUptime, snsServicesEntry=snsServicesEntry, snsServicesName=snsServicesName, PYSNMP_MODULE_ID=snsServices, snsServicesIndex=snsServicesIndex, snsServices=snsServices)
