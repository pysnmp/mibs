#
# PySNMP MIB module MSERIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/smartoptics/MSERIES-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 10:10:26 2024
# On host fv-az1771-969 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, iso, IpAddress, NotificationType, Integer32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, MibIdentifier, Counter32, ModuleIdentity, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "iso", "IpAddress", "NotificationType", "Integer32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "MibIdentifier", "Counter32", "ModuleIdentity", "ObjectIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
smartoptics = ModuleIdentity((1, 3, 6, 1, 4, 1, 30826))
smartoptics.setRevisions(('2014-02-12 13:27',))
if mibBuilder.loadTexts: smartoptics.setLastUpdated('201402121327Z')
if mibBuilder.loadTexts: smartoptics.setOrganization('SmartOptics')
mseries = ObjectIdentity((1, 3, 6, 1, 4, 1, 30826, 1))
if mibBuilder.loadTexts: mseries.setStatus('current')
mibBuilder.exportSymbols("MSERIES-MIB", mseries=mseries, smartoptics=smartoptics, PYSNMP_MODULE_ID=smartoptics)
