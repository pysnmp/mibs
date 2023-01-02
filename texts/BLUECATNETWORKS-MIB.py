#
# PySNMP MIB module BLUECATNETWORKS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BLUECATNETWORKS-MIB
# Produced by pysmi-1.1.8 at Mon Jan  2 15:24:29 2023
# On host fv-az407-858 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, ObjectIdentity, enterprises, TimeTicks, Bits, iso, IpAddress, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "ObjectIdentity", "enterprises", "TimeTicks", "Bits", "iso", "IpAddress", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "NotificationType", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bluecatnetworksId = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 1))
bluecatnetworksId.setRevisions(('2010-11-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bluecatnetworksId.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: bluecatnetworksId.setLastUpdated('201011300000Z')
if mibBuilder.loadTexts: bluecatnetworksId.setOrganization('BlueCat Networks Inc.')
if mibBuilder.loadTexts: bluecatnetworksId.setContactInfo('BlueCat Networks Inc.\n\t\t \n\t\t Tel: +1 866 491 2228 (toll free)\n\t\t      +1 416 646 8400 (international) \n\t\t Email: support@bluecatnetworks.com')
if mibBuilder.loadTexts: bluecatnetworksId.setDescription('New oid assignments for Cisco REPEATER MIB and others.')
bluecatnetworks = MibIdentifier((1, 3, 6, 1, 4, 1, 13315))
appliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100))
mibBuilder.exportSymbols("BLUECATNETWORKS-MIB", bluecatnetworksId=bluecatnetworksId, bluecatnetworks=bluecatnetworks, PYSNMP_MODULE_ID=bluecatnetworksId, appliances=appliances)
