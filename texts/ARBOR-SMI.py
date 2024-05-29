#
# PySNMP MIB module ARBOR-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arbornet/ARBORNET-SMI
# Produced by pysmi-1.1.12 at Wed May 29 10:51:25 2024
# On host fv-az1206-254 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, enterprises, ObjectIdentity, Unsigned32, IpAddress, Counter64, Gauge32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, MibIdentifier, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "enterprises", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter64", "Gauge32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "MibIdentifier", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
arbornetworks = ModuleIdentity((1, 3, 6, 1, 4, 1, 9694))
arbornetworks.setRevisions(('2013-11-14 00:00', '2013-08-19 00:00', '2011-07-20 00:00', '2009-03-30 00:00', '2008-11-13 00:00', '2005-09-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: arbornetworks.setRevisionsDescriptions(('Add peakflowMobile product.', 'Updated contact information', 'Added pravail productid.', 'Update contact group name.', 'Update company address. Add arborExperimental.', 'Apply fixes from validation.',))
if mibBuilder.loadTexts: arbornetworks.setLastUpdated('201311140000Z')
if mibBuilder.loadTexts: arbornetworks.setOrganization('Arbor Networks, Inc.')
if mibBuilder.loadTexts: arbornetworks.setContactInfo('\tArbor Networks, Inc.\n\t\t\t\tArbor Technical Assistance Center\n\n\t\t\t\tPostal: 76 Blanchard Road\n\t\t\t\t\tBurlington, MA 01803\n\t\t\t\t\tUSA\n\n\t\t\t\tTel: +1 866 212 7267 (toll free)\n\t\t\t\t     +1 781 362 4300\n\t\t\t\tEmail: support@arbor.net ')
if mibBuilder.loadTexts: arbornetworks.setDescription('The Structure of Management Information for the\n\t\tArbor Networks enterprise.')
arbornetworksProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9694, 1))
if mibBuilder.loadTexts: arbornetworksProducts.setStatus('current')
if mibBuilder.loadTexts: arbornetworksProducts.setDescription('arbornetworksProducts provides a root object identifier\n\t\tfrom which MODULE-IDENTITY values may be assigned.')
arborExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 9694, 2))
if mibBuilder.loadTexts: arborExperimental.setStatus('current')
if mibBuilder.loadTexts: arborExperimental.setDescription('arborExperimental provides a root object identifier\n\t\t from which MODULE-IDENTITY for experimental purposes\n\t\t may be assigned.')
mibBuilder.exportSymbols("ARBOR-SMI", arbornetworksProducts=arbornetworksProducts, PYSNMP_MODULE_ID=arbornetworks, arborExperimental=arborExperimental, arbornetworks=arbornetworks)
