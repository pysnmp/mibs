#
# PySNMP MIB module NORTEL-OPTICAL-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/NORTEL-OPTICAL-GENERIC-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 15:56:17 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
nortel, = mibBuilder.importSymbols("NORTEL-MIB", "nortel")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Counter64, TimeTicks, Bits, ObjectIdentity, Gauge32, Unsigned32, ModuleIdentity, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Counter64", "TimeTicks", "Bits", "ObjectIdentity", "Gauge32", "Unsigned32", "ModuleIdentity", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nnOpticalGenericMIBs = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 68, 10))
nnOpticalGenericMIBs.setRevisions(('2005-07-12 00:00', '2008-02-07 00:00',))
if mibBuilder.loadTexts: nnOpticalGenericMIBs.setLastUpdated('200802070000Z')
if mibBuilder.loadTexts: nnOpticalGenericMIBs.setOrganization('Nortel')
opterametro = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68))
mibBuilder.exportSymbols("NORTEL-OPTICAL-GENERIC-MIB", PYSNMP_MODULE_ID=nnOpticalGenericMIBs, opterametro=opterametro, nnOpticalGenericMIBs=nnOpticalGenericMIBs)
