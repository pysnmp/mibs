#
# PySNMP MIB module TAIT-INFRA93-94SERIES-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-INFRA93-94SERIES-COMMON-MIB
# Produced by pysmi-1.1.8 at Thu Jan  6 19:50:32 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, Gauge32, MibIdentifier, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, IpAddress, Counter32, Bits, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Gauge32", "MibIdentifier", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "IpAddress", "Counter32", "Bits", "Unsigned32", "ObjectIdentity")
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
