#
# PySNMP MIB module NET-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netsnmp/NET-SNMP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 17:13:31 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Counter32, NotificationType, IpAddress, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Integer32, Bits, Unsigned32, Counter64, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter32", "NotificationType", "IpAddress", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Integer32", "Bits", "Unsigned32", "Counter64", "MibIdentifier", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("NET-SNMP-MIB", netSnmpExperimental=netSnmpExperimental, netSnmpCompliances=netSnmpCompliances, netSnmpConformance=netSnmpConformance, PYSNMP_MODULE_ID=netSnmp, netSnmpModuleIDs=netSnmpModuleIDs, netSnmpNotificationPrefix=netSnmpNotificationPrefix, netSnmpObjects=netSnmpObjects, netSnmp=netSnmp, netSnmpEnumerations=netSnmpEnumerations, netSnmpNotifications=netSnmpNotifications, netSnmpNotificationObjects=netSnmpNotificationObjects, netSnmpGroups=netSnmpGroups, netSnmpPlaypen=netSnmpPlaypen, netSnmpDomains=netSnmpDomains, netSnmpAgentOIDs=netSnmpAgentOIDs)
