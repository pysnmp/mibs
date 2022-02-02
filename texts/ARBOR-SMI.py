#
# PySNMP MIB module ARBOR-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arbornet/ARBORNET-SMI
# Produced by pysmi-1.1.8 at Wed Feb  2 18:18:39 2022
# On host fv-az83-345 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, enterprises, TimeTicks, Gauge32, MibIdentifier, Bits, ObjectIdentity, ModuleIdentity, NotificationType, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "enterprises", "TimeTicks", "Gauge32", "MibIdentifier", "Bits", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ARBOR-SMI", arbornetworks=arbornetworks, arbornetworksProducts=arbornetworksProducts, arborExperimental=arborExperimental, PYSNMP_MODULE_ID=arbornetworks)
