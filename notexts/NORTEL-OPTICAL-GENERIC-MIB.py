#
# PySNMP MIB module NORTEL-OPTICAL-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/NORTEL-OPTICAL-GENERIC-MIB
# Produced by pysmi-1.1.8 at Thu Jan 27 21:15:54 2022
# On host fv-az74-168 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
nortel, = mibBuilder.importSymbols("NORTEL-MIB", "nortel")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, MibIdentifier, ObjectIdentity, Unsigned32, Gauge32, IpAddress, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Gauge32", "IpAddress", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nnOpticalGenericMIBs = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 68, 10))
nnOpticalGenericMIBs.setRevisions(('2005-07-12 00:00', '2008-02-07 00:00',))
if mibBuilder.loadTexts: nnOpticalGenericMIBs.setLastUpdated('200802070000Z')
if mibBuilder.loadTexts: nnOpticalGenericMIBs.setOrganization('Nortel')
opterametro = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68))
mibBuilder.exportSymbols("NORTEL-OPTICAL-GENERIC-MIB", opterametro=opterametro, nnOpticalGenericMIBs=nnOpticalGenericMIBs, PYSNMP_MODULE_ID=nnOpticalGenericMIBs)
