#
# PySNMP MIB module NET-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netsnmp/NET-SNMP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 19:49:05 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, MibIdentifier, Counter32, Integer32, Gauge32, Counter64, enterprises, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, TimeTicks, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "MibIdentifier", "Counter32", "Integer32", "Gauge32", "Counter64", "enterprises", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "TimeTicks", "iso", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netSnmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072))
netSnmp.setRevisions(('2002-01-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netSnmp.setRevisionsDescriptions(('First draft',))
if mibBuilder.loadTexts: netSnmp.setLastUpdated('200201300000Z')
if mibBuilder.loadTexts: netSnmp.setOrganization('www.net-snmp.org')
if mibBuilder.loadTexts: netSnmp.setContactInfo('postal:   Wes Hardaker\n                    P.O. Box 382\n                    Davis CA  95617\n\n          email:    net-snmp-coders@lists.sourceforge.net')
if mibBuilder.loadTexts: netSnmp.setDescription('Top-level infrastructure of the Net-SNMP project enterprise MIB tree')
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
mibBuilder.exportSymbols("NET-SNMP-MIB", netSnmp=netSnmp, netSnmpPlaypen=netSnmpPlaypen, netSnmpAgentOIDs=netSnmpAgentOIDs, netSnmpModuleIDs=netSnmpModuleIDs, netSnmpEnumerations=netSnmpEnumerations, PYSNMP_MODULE_ID=netSnmp, netSnmpObjects=netSnmpObjects, netSnmpDomains=netSnmpDomains, netSnmpNotificationObjects=netSnmpNotificationObjects, netSnmpConformance=netSnmpConformance, netSnmpCompliances=netSnmpCompliances, netSnmpNotifications=netSnmpNotifications, netSnmpGroups=netSnmpGroups, netSnmpNotificationPrefix=netSnmpNotificationPrefix, netSnmpExperimental=netSnmpExperimental)
