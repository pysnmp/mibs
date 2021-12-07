#
# PySNMP MIB module PAN-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-GLOBAL-REG-MIB
# Produced by pysmi-1.1.3 at Tue Dec  7 14:03:30 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, Integer32, Counter32, Counter64, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, IpAddress, iso, enterprises, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Integer32", "Counter32", "Counter64", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "IpAddress", "iso", "enterprises", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
panGlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 1))
panGlobalRegModule.setRevisions(('2011-02-09 16:10',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: panGlobalRegModule.setRevisionsDescriptions(('\n\t\t\tRev 1.0\n\t\t\tInitial version of MIB module PAN-GLOBAL-REG.',))
if mibBuilder.loadTexts: panGlobalRegModule.setLastUpdated('201106271040Z')
if mibBuilder.loadTexts: panGlobalRegModule.setOrganization('Palo Alto Networks')
if mibBuilder.loadTexts: panGlobalRegModule.setContactInfo('\n\t\t\t\t\tCustomer Support\n\t\t\t\t\tPalo Alto Networks\n\t\t\t\t\t4401 Great America Pkwy\n\t\t\t\t\tSanta Clara, CA 95054-1211\n\n\t\t\t\t\t+1 866-898-9087\n\t\t\t\t\tsupport at paloaltonetworks dot com')
if mibBuilder.loadTexts: panGlobalRegModule.setDescription("\n\t\t\tA MIB module containing top-level OID definitions\n\t\t\tfor various sub-trees for Palo Alto Networks' enterprise MIB modules.")
panRoot = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461))
if mibBuilder.loadTexts: panRoot.setStatus('current')
if mibBuilder.loadTexts: panRoot.setDescription('\n\t\t\tThe root of the OID sub-tree assigned to Palo Alto Networks assigned by\n\t\t\tthe Internet Assigned Numbers Authority (IANA).')
panReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 1))
if mibBuilder.loadTexts: panReg.setStatus('current')
if mibBuilder.loadTexts: panReg.setDescription('\n\t\t\tSub-tree for registrations - identification of modules and logical and\n\t\t\tphysical components.')
panModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1))
if mibBuilder.loadTexts: panModules.setStatus('current')
if mibBuilder.loadTexts: panModules.setDescription('\n\t\t\tSub-tree for module registrations.')
panMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2))
if mibBuilder.loadTexts: panMibs.setStatus('current')
if mibBuilder.loadTexts: panMibs.setDescription('\n\t\t\tSub-tree for all Palo Alto object and event definitions.')
panCommonMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 1))
if mibBuilder.loadTexts: panCommonMib.setStatus('current')
if mibBuilder.loadTexts: panCommonMib.setDescription('\n\t\t\tSub-tree for common Palo Alto object and event definitions.\n\t\t\tThese would be implemented by all Palo Alto products.')
panSpecificMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 2))
if mibBuilder.loadTexts: panSpecificMib.setStatus('current')
if mibBuilder.loadTexts: panSpecificMib.setDescription('\n\t\t\tSub-tree for specific Palo Alto object and event definitions.')
panProductsMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3))
if mibBuilder.loadTexts: panProductsMibs.setStatus('current')
if mibBuilder.loadTexts: panProductsMibs.setDescription('\n\t\t\tSub-tree for all Palo Alto product specific definitions.')
mibBuilder.exportSymbols("PAN-GLOBAL-REG", panGlobalRegModule=panGlobalRegModule, panProductsMibs=panProductsMibs, panModules=panModules, panReg=panReg, panMibs=panMibs, panSpecificMib=panSpecificMib, panRoot=panRoot, PYSNMP_MODULE_ID=panGlobalRegModule, panCommonMib=panCommonMib)
