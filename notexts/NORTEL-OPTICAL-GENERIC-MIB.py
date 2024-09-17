#
# PySNMP MIB module NORTEL-OPTICAL-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/NORTEL-OPTICAL-GENERIC-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:26:09 2024
# On host fv-az1019-803 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
nortel, = mibBuilder.importSymbols("NORTEL-MIB", "nortel")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, Unsigned32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, Bits, IpAddress, ModuleIdentity, MibIdentifier, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Unsigned32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "Bits", "IpAddress", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nnOpticalGenericMIBs = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 68, 10))
nnOpticalGenericMIBs.setRevisions(('2005-07-12 00:00', '2008-02-07 00:00',))
if mibBuilder.loadTexts: nnOpticalGenericMIBs.setLastUpdated('200802070000Z')
if mibBuilder.loadTexts: nnOpticalGenericMIBs.setOrganization('Nortel')
opterametro = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68))
mibBuilder.exportSymbols("NORTEL-OPTICAL-GENERIC-MIB", nnOpticalGenericMIBs=nnOpticalGenericMIBs, PYSNMP_MODULE_ID=nnOpticalGenericMIBs, opterametro=opterametro)
