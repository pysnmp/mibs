#
# PySNMP MIB module MDS-ORBIT-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-ORBIT-SMI-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 23:16:19 2022
# On host fv-az42-507 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
mdsRoot, = mibBuilder.importSymbols("MDS-REG-MIB", "mdsRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, ModuleIdentity, Bits, Counter32, NotificationType, Counter64, Gauge32, iso, Unsigned32, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Bits", "Counter32", "NotificationType", "Counter64", "Gauge32", "iso", "Unsigned32", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mdsOrbit = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10))
mdsOrbit.setRevisions(('2013-04-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mdsOrbit.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: mdsOrbit.setLastUpdated('201304220000Z')
if mibBuilder.loadTexts: mdsOrbit.setOrganization('GE MDS LLC\n        http://www.gemds.com')
if mibBuilder.loadTexts: mdsOrbit.setContactInfo('T 1-800-474-0694 (Toll Free in North America)\n         T 585-242-9600\n         F 585-242-9620\n\n         175 Science Parkway\n         Rochester, New York 14620\n         USA')
if mibBuilder.loadTexts: mdsOrbit.setDescription('The structure of Management Information for the GE MDS.')
mdsSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 1))
if mibBuilder.loadTexts: mdsSystem.setStatus('current')
if mibBuilder.loadTexts: mdsSystem.setDescription('mdsSystem provides root Object Identifier for Management\n         Information Base for system related configuration like\n         NTP, DNS etc')
mdsInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 2))
if mibBuilder.loadTexts: mdsInterfaces.setStatus('current')
if mibBuilder.loadTexts: mdsInterfaces.setDescription('mdsInterfaces provides root Object Identifier for Management\n         Information Base for extended information about various\n         wired/wireless/virtual interfaces on MDS products.')
mdsServices = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 3))
if mibBuilder.loadTexts: mdsServices.setStatus('current')
if mibBuilder.loadTexts: mdsServices.setDescription('mdsServices provides root Object Identifier for Management\n         Information Base for various network and application services\n         on MDS products.')
mdsLogging = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 4))
if mibBuilder.loadTexts: mdsLogging.setStatus('current')
if mibBuilder.loadTexts: mdsLogging.setDescription('mdsLogging provides root Object Identifier for Management\n         Information Base for logging functionality on MDS products.')
mibBuilder.exportSymbols("MDS-ORBIT-SMI-MIB", mdsInterfaces=mdsInterfaces, mdsServices=mdsServices, PYSNMP_MODULE_ID=mdsOrbit, mdsOrbit=mdsOrbit, mdsLogging=mdsLogging, mdsSystem=mdsSystem)
