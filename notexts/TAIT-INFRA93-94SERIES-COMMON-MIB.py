#
# PySNMP MIB module TAIT-INFRA93-94SERIES-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-INFRA93-94SERIES-COMMON-MIB
# Produced by pysmi-1.1.8 at Tue Jan 11 21:45:40 2022
# On host fv-az74-997 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Bits, IpAddress, TimeTicks, Counter32, Unsigned32, ModuleIdentity, Integer32, MibIdentifier, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Bits", "IpAddress", "TimeTicks", "Counter32", "Unsigned32", "ModuleIdentity", "Integer32", "MibIdentifier", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
taitModules, = mibBuilder.importSymbols("TAIT-COMMON-MIB", "taitModules")
infra93_94MibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1, 10)).setLabel("infra93-94MibModule")
infra93_94MibModule.setRevisions(('2014-06-17 11:00', '2014-01-26 00:00', '2014-01-14 11:00',))
if mibBuilder.loadTexts: infra93_94MibModule.setLastUpdated('201406171100Z')
if mibBuilder.loadTexts: infra93_94MibModule.setOrganization('www.taitradio.com')
mibBuilder.exportSymbols("TAIT-INFRA93-94SERIES-COMMON-MIB", infra93_94MibModule=infra93_94MibModule, PYSNMP_MODULE_ID=infra93_94MibModule)
