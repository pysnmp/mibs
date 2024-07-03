#
# PySNMP MIB module NORTEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/NORTEL-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 12:26:23 2024
# On host fv-az1022-995 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter64, NotificationType, IpAddress, Bits, TimeTicks, Integer32, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter32, Unsigned32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "NotificationType", "IpAddress", "Bits", "TimeTicks", "Integer32", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter32", "Unsigned32", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nortel = ModuleIdentity((1, 3, 6, 1, 4, 1, 562))
if mibBuilder.loadTexts: nortel.setLastUpdated('200305010000Z')
if mibBuilder.loadTexts: nortel.setOrganization('Northern Telecom Ltd.')
nortelGenericMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 29))
opterametro = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68))
mibBuilder.exportSymbols("NORTEL-MIB", opterametro=opterametro, nortelGenericMIBs=nortelGenericMIBs, PYSNMP_MODULE_ID=nortel, nortel=nortel)
