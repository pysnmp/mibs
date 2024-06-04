#
# PySNMP MIB module NORTEL-OPTICAL-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/NORTEL-OPTICAL-GENERIC-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 10:09:20 2024
# On host fv-az1773-903 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
nortel, = mibBuilder.importSymbols("NORTEL-MIB", "nortel")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter64, IpAddress, MibIdentifier, NotificationType, Bits, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, ObjectIdentity, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "IpAddress", "MibIdentifier", "NotificationType", "Bits", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "Gauge32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nnOpticalGenericMIBs = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 68, 10))
nnOpticalGenericMIBs.setRevisions(('2005-07-12 00:00', '2008-02-07 00:00',))
if mibBuilder.loadTexts: nnOpticalGenericMIBs.setLastUpdated('200802070000Z')
if mibBuilder.loadTexts: nnOpticalGenericMIBs.setOrganization('Nortel')
opterametro = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68))
mibBuilder.exportSymbols("NORTEL-OPTICAL-GENERIC-MIB", PYSNMP_MODULE_ID=nnOpticalGenericMIBs, opterametro=opterametro, nnOpticalGenericMIBs=nnOpticalGenericMIBs)
