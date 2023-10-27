#
# PySNMP MIB module BENU-WAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-WAG-MIB
# Produced by pysmi-1.1.10 at Fri Oct 27 07:36:09 2023
# On host fv-az1236-588 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
benuPlatSerMIB, = mibBuilder.importSymbols("BENU-PLATFORM-SERVICE-MIB", "benuPlatSerMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Counter32, ModuleIdentity, iso, Gauge32, Counter64, MibIdentifier, Unsigned32, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Counter32", "ModuleIdentity", "iso", "Gauge32", "Counter64", "MibIdentifier", "Unsigned32", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuWAG = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1))
benuWAG.setRevisions(('2012-10-08 00:00',))
if mibBuilder.loadTexts: benuWAG.setLastUpdated('201210080000Z')
if mibBuilder.loadTexts: benuWAG.setOrganization('Benu Networks')
mibBuilder.exportSymbols("BENU-WAG-MIB", benuWAG=benuWAG, PYSNMP_MODULE_ID=benuWAG)
