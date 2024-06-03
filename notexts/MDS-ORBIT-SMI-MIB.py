#
# PySNMP MIB module MDS-ORBIT-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-ORBIT-SMI-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 12:23:38 2024
# On host fv-az1530-743 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
mdsRoot, = mibBuilder.importSymbols("MDS-REG-MIB", "mdsRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Counter64, Integer32, Unsigned32, Counter32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, iso, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Counter64", "Integer32", "Unsigned32", "Counter32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "iso", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mdsOrbit = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10))
mdsOrbit.setRevisions(('2013-04-22 00:00',))
if mibBuilder.loadTexts: mdsOrbit.setLastUpdated('201304220000Z')
if mibBuilder.loadTexts: mdsOrbit.setOrganization('GE MDS LLC http://www.gemds.com')
mdsSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 1))
if mibBuilder.loadTexts: mdsSystem.setStatus('current')
mdsInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 2))
if mibBuilder.loadTexts: mdsInterfaces.setStatus('current')
mdsServices = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 3))
if mibBuilder.loadTexts: mdsServices.setStatus('current')
mdsLogging = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 4))
if mibBuilder.loadTexts: mdsLogging.setStatus('current')
mibBuilder.exportSymbols("MDS-ORBIT-SMI-MIB", mdsOrbit=mdsOrbit, mdsInterfaces=mdsInterfaces, mdsLogging=mdsLogging, PYSNMP_MODULE_ID=mdsOrbit, mdsSystem=mdsSystem, mdsServices=mdsServices)
