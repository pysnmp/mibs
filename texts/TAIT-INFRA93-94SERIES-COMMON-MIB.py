#
# PySNMP MIB module TAIT-INFRA93-94SERIES-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-INFRA93-94SERIES-COMMON-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 13:34:35 2024
# On host fv-az883-167 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Integer32, NotificationType, TimeTicks, Unsigned32, Gauge32, IpAddress, MibIdentifier, iso, Counter32, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "NotificationType", "TimeTicks", "Unsigned32", "Gauge32", "IpAddress", "MibIdentifier", "iso", "Counter32", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
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
