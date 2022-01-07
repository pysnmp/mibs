#
# PySNMP MIB module NET-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netsnmp/NET-SNMP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:12:57 2022
# On host fv-az77-763 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Bits, Counter64, iso, Gauge32, ObjectIdentity, Unsigned32, Integer32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Bits", "Counter64", "iso", "Gauge32", "ObjectIdentity", "Unsigned32", "Integer32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netSnmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072))
netSnmp.setRevisions(('2002-01-30 00:00',))
if mibBuilder.loadTexts: netSnmp.setLastUpdated('200201300000Z')
if mibBuilder.loadTexts: netSnmp.setOrganization('www.net-snmp.org')
netSnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1))
netSnmpEnumerations = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3))
netSnmpModuleIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1))
netSnmpAgentOIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2))
netSnmpDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3))
netSnmpExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 9999))
netSnmpPlaypen = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 9999, 9999))
netSnmpNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 4))
netSnmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 4, 0))
netSnmpNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 4, 1))
netSnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 5))
netSnmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 5, 1))
netSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 5, 2))
mibBuilder.exportSymbols("NET-SNMP-MIB", netSnmpConformance=netSnmpConformance, netSnmpAgentOIDs=netSnmpAgentOIDs, netSnmpGroups=netSnmpGroups, netSnmpNotificationObjects=netSnmpNotificationObjects, netSnmpNotificationPrefix=netSnmpNotificationPrefix, netSnmpModuleIDs=netSnmpModuleIDs, netSnmp=netSnmp, PYSNMP_MODULE_ID=netSnmp, netSnmpObjects=netSnmpObjects, netSnmpExperimental=netSnmpExperimental, netSnmpDomains=netSnmpDomains, netSnmpNotifications=netSnmpNotifications, netSnmpEnumerations=netSnmpEnumerations, netSnmpPlaypen=netSnmpPlaypen, netSnmpCompliances=netSnmpCompliances)
