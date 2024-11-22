#
# PySNMP MIB module MDS-ORBIT-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-ORBIT-SMI-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 16:00:20 2024
# On host fv-az1245-338 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
mdsRoot, = mibBuilder.importSymbols("MDS-REG-MIB", "mdsRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Integer32, Counter64, Gauge32, MibIdentifier, Unsigned32, IpAddress, Bits, ObjectIdentity, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Integer32", "Counter64", "Gauge32", "MibIdentifier", "Unsigned32", "IpAddress", "Bits", "ObjectIdentity", "Counter32", "ModuleIdentity")
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
mibBuilder.exportSymbols("MDS-ORBIT-SMI-MIB", mdsSystem=mdsSystem, PYSNMP_MODULE_ID=mdsOrbit, mdsOrbit=mdsOrbit, mdsLogging=mdsLogging, mdsInterfaces=mdsInterfaces, mdsServices=mdsServices)
