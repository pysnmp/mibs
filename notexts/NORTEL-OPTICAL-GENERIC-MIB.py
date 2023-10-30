#
# PySNMP MIB module NORTEL-OPTICAL-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/NORTEL-OPTICAL-GENERIC-MIB
# Produced by pysmi-1.1.10 at Mon Oct 30 02:27:13 2023
# On host fv-az882-479 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
nortel, = mibBuilder.importSymbols("NORTEL-MIB", "nortel")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, iso, Bits, TimeTicks, ModuleIdentity, Unsigned32, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "iso", "Bits", "TimeTicks", "ModuleIdentity", "Unsigned32", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nnOpticalGenericMIBs = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 68, 10))
nnOpticalGenericMIBs.setRevisions(('2005-07-12 00:00', '2008-02-07 00:00',))
if mibBuilder.loadTexts: nnOpticalGenericMIBs.setLastUpdated('200802070000Z')
if mibBuilder.loadTexts: nnOpticalGenericMIBs.setOrganization('Nortel')
opterametro = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68))
mibBuilder.exportSymbols("NORTEL-OPTICAL-GENERIC-MIB", PYSNMP_MODULE_ID=nnOpticalGenericMIBs, opterametro=opterametro, nnOpticalGenericMIBs=nnOpticalGenericMIBs)
