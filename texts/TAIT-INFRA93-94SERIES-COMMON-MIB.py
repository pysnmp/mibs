#
# PySNMP MIB module TAIT-INFRA93-94SERIES-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-INFRA93-94SERIES-COMMON-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:23:39 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, ObjectIdentity, Unsigned32, TimeTicks, Counter64, NotificationType, Bits, iso, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "TimeTicks", "Counter64", "NotificationType", "Bits", "iso", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
taitModules, = mibBuilder.importSymbols("TAIT-COMMON-MIB", "taitModules")
infra93_94MibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1, 10)).setLabel("infra93-94MibModule")
infra93_94MibModule.setRevisions(('2014-06-17 11:00', '2014-01-26 00:00', '2014-01-14 11:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: infra93_94MibModule.setRevisionsDescriptions(('Define the module and product root OIDs for monitored Tait 93/94-series Base Stations', '1.04.00 - Remove unused import', '1.01.01 - Initial version prior to change log entries',))
if mibBuilder.loadTexts: infra93_94MibModule.setLastUpdated('201406171100Z')
if mibBuilder.loadTexts: infra93_94MibModule.setOrganization('www.taitradio.com')
if mibBuilder.loadTexts: infra93_94MibModule.setContactInfo('Tait Communications\n                     245 Wooldridge Road\n                     PO Box 1645\n                     Christchurch\n                     New Zealand\n\n             phone:  +64 3358 3399\n             email:  support@taitradio.com')
if mibBuilder.loadTexts: infra93_94MibModule.setDescription('Add system alarms for TDMA.')
mibBuilder.exportSymbols("TAIT-INFRA93-94SERIES-COMMON-MIB", infra93_94MibModule=infra93_94MibModule, PYSNMP_MODULE_ID=infra93_94MibModule)
