#
# PySNMP MIB module ACCEDIAN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACCEDIAN-SMI
# Produced by pysmi-1.1.12 at Wed Jul  3 11:59:30 2024
# On host fv-az768-763 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, TimeTicks, Counter32, Gauge32, IpAddress, iso, ObjectIdentity, Integer32, MibIdentifier, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "TimeTicks", "Counter32", "Gauge32", "IpAddress", "iso", "ObjectIdentity", "Integer32", "MibIdentifier", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ACCEDIAN-SMI", acdMibs=acdMibs, accedianMIB=accedianMIB, acdProducts=acdProducts, acdExperiment=acdExperiment, acdTraps=acdTraps, acdServices=acdServices, PYSNMP_MODULE_ID=accedianMIB)
