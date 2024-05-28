#
# PySNMP MIB module MSERIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/smartoptics/MSERIES-MIB
# Produced by pysmi-1.1.12 at Tue May 28 12:12:03 2024
# On host fv-az1490-484 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Integer32, MibIdentifier, TimeTicks, iso, enterprises, Counter64, Bits, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Integer32", "MibIdentifier", "TimeTicks", "iso", "enterprises", "Counter64", "Bits", "Gauge32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
smartoptics = ModuleIdentity((1, 3, 6, 1, 4, 1, 30826))
smartoptics.setRevisions(('2014-02-12 13:27',))
if mibBuilder.loadTexts: smartoptics.setLastUpdated('201402121327Z')
if mibBuilder.loadTexts: smartoptics.setOrganization('SmartOptics')
mseries = ObjectIdentity((1, 3, 6, 1, 4, 1, 30826, 1))
if mibBuilder.loadTexts: mseries.setStatus('current')
mibBuilder.exportSymbols("MSERIES-MIB", PYSNMP_MODULE_ID=smartoptics, smartoptics=smartoptics, mseries=mseries)
