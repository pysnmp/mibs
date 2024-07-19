#
# PySNMP MIB module HIPATH-WIRELESS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ewc/HIPATH-WIRELESS-SMI
# Produced by pysmi-1.1.12 at Fri Jul 19 10:02:00 2024
# On host fv-az1251-884 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, Gauge32, Integer32, Counter64, Unsigned32, Counter32, iso, NotificationType, enterprises, TimeTicks, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "Gauge32", "Integer32", "Counter64", "Unsigned32", "Counter32", "iso", "NotificationType", "enterprises", "TimeTicks", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hiPathWireless = ModuleIdentity((1, 3, 6, 1, 4, 1, 4329, 15))
hiPathWireless.setRevisions(('2005-07-21 02:37',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hiPathWireless.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hiPathWireless.setLastUpdated('200507210237Z')
if mibBuilder.loadTexts: hiPathWireless.setOrganization('Chantry Networks, Inc.')
if mibBuilder.loadTexts: hiPathWireless.setContactInfo('Behrouz Sultan\n\t\t\t\tChantry Networks, Inc.\n\t\t\t\t\n\t\t\t\t1900 Minnesota Court, Suite 125\n\t\t\t\tMississauga ON, L5N 3C9\n\t\t\t\t\n\t\t\t\tEmail: behrouz.sultan@siemens.com\n\t\t\t\tPhone 1-905-363-6400\n\t\t\t\tFax   1-905-567-0099')
if mibBuilder.loadTexts: hiPathWireless.setDescription('The root MIB module for High Path Wireless Products.\n\t\t\t\tenterprises.siemens(4329).15')
siemens = MibIdentifier((1, 3, 6, 1, 4, 1, 4329))
hiPathWirelessProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1))
if mibBuilder.loadTexts: hiPathWirelessProducts.setStatus('current')
if mibBuilder.loadTexts: hiPathWirelessProducts.setDescription('Provides a root OID from which MIB-II sysObjectID values \n\t\t\t\tare assigned. Actual product OIDs are defined in\n\t\t\t\tHIPATH-WIRELESS-PRODUCTS-MIB.')
hiPathWirelessMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 3))
if mibBuilder.loadTexts: hiPathWirelessMgmt.setStatus('current')
if mibBuilder.loadTexts: hiPathWirelessMgmt.setDescription('Main subtree for High Path Wireless Networks management information.')
hiPathWirelessDevelopment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 4))
if mibBuilder.loadTexts: hiPathWirelessDevelopment.setStatus('current')
if mibBuilder.loadTexts: hiPathWirelessDevelopment.setDescription("Subtree for pre-release MIB development. \n\t\t\t\tElements in this subtree are eventually moved to \n\t\t\t\t'hiPathWirelessMgmt'.")
hiPathWirelessModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 5))
if mibBuilder.loadTexts: hiPathWirelessModules.setStatus('current')
if mibBuilder.loadTexts: hiPathWirelessModules.setDescription('Provides a root object identifier from which\n\t\t\t\tMODULE-IDENTITY values are assigned.')
hiPathWirelessHWM = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 6))
if mibBuilder.loadTexts: hiPathWirelessHWM.setStatus('current')
if mibBuilder.loadTexts: hiPathWirelessHWM.setDescription('Sub-tree for Hipath Wireless Manager Application and its associated applications.')
mibBuilder.exportSymbols("HIPATH-WIRELESS-SMI", hiPathWirelessModules=hiPathWirelessModules, hiPathWirelessProducts=hiPathWirelessProducts, hiPathWirelessHWM=hiPathWirelessHWM, hiPathWirelessMgmt=hiPathWirelessMgmt, PYSNMP_MODULE_ID=hiPathWireless, hiPathWireless=hiPathWireless, siemens=siemens, hiPathWirelessDevelopment=hiPathWirelessDevelopment)
