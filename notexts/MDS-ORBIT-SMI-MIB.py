#
# PySNMP MIB module MDS-ORBIT-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-ORBIT-SMI-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 10:00:41 2024
# On host fv-az1427-100 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
mdsRoot, = mibBuilder.importSymbols("MDS-REG-MIB", "mdsRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibIdentifier, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Counter32, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Counter32", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MDS-ORBIT-SMI-MIB", mdsOrbit=mdsOrbit, mdsLogging=mdsLogging, mdsServices=mdsServices, PYSNMP_MODULE_ID=mdsOrbit, mdsSystem=mdsSystem, mdsInterfaces=mdsInterfaces)
