#
# PySNMP MIB module ACCEDIAN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACCEDIAN-SMI
# Produced by pysmi-1.1.8 at Fri Jan  7 15:09:51 2022
# On host fv-az42-180 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, ModuleIdentity, Gauge32, Integer32, iso, Unsigned32, ObjectIdentity, IpAddress, TimeTicks, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "ModuleIdentity", "Gauge32", "Integer32", "iso", "Unsigned32", "ObjectIdentity", "IpAddress", "TimeTicks", "MibIdentifier", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
accedianMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420))
accedianMIB.setRevisions(('2006-08-06 01:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: accedianMIB.setRevisionsDescriptions(('Initial version of MIB module ACCEDIAN-SMI.',))
if mibBuilder.loadTexts: accedianMIB.setLastUpdated('200608060100Z')
if mibBuilder.loadTexts: accedianMIB.setOrganization('Accedian Networks, Inc.')
if mibBuilder.loadTexts: accedianMIB.setContactInfo('Accedian Technical Assistance Center\n             Accedian Networks, Inc.\n             4878 Levy, suite 202\n             Saint-Laurent, Quebec Canada H4R 2P1\n             E-mail: support@accedian.com')
if mibBuilder.loadTexts: accedianMIB.setDescription('The Structure of Management Information for Accedian Networks.')
acdProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 22420, 1))
if mibBuilder.loadTexts: acdProducts.setStatus('current')
if mibBuilder.loadTexts: acdProducts.setDescription("The root of Accedian's Product OIDs.")
acdMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 22420, 2))
if mibBuilder.loadTexts: acdMibs.setStatus('current')
if mibBuilder.loadTexts: acdMibs.setDescription("The root of Accedian's MIB objects.")
acdTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 22420, 3))
if mibBuilder.loadTexts: acdTraps.setStatus('current')
if mibBuilder.loadTexts: acdTraps.setDescription("The root of Accedian's Trap OIDs.")
acdExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 4))
acdServices = ObjectIdentity((1, 3, 6, 1, 4, 1, 22420, 5))
if mibBuilder.loadTexts: acdServices.setStatus('current')
if mibBuilder.loadTexts: acdServices.setDescription("The root of Accedian's Services OIDs.")
mibBuilder.exportSymbols("ACCEDIAN-SMI", accedianMIB=accedianMIB, PYSNMP_MODULE_ID=accedianMIB, acdProducts=acdProducts, acdTraps=acdTraps, acdMibs=acdMibs, acdServices=acdServices, acdExperiment=acdExperiment)
