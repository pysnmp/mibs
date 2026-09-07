#
# PySNMP MIB module CISCO-DMN-DSG-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DMN-DSG-ROOT-MIB
# Source digest sha256:9e2ea41daf0b6f71a96109730c701120aab2d75ff6d0b6ef7ddabb0c69ae915d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSPVTG = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429))
ciscoSPVTG.setRevisions(('2010-08-30 11:00', '2009-11-26 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSPVTG.setRevisionsDescriptions(('V01.00.01 2010-08-30\n                    Updated for adherence to SNMPv2 format.', 'V01.00.00 2009-11-26\n                    Initial Version.',))
if mibBuilder.loadTexts: ciscoSPVTG.setLastUpdated('2010-08-30 11:00')
if mibBuilder.loadTexts: ciscoSPVTG.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSPVTG.setContactInfo('Cisco Systems, Inc.\n        Customer Service \n        Postal: 170 W Tasman Drive\n        San Jose, CA 95134\n        USA  \n        Tel: +1 800 553 NETS\n        \n        E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoSPVTG.setDescription('Cisco top level MIB.')
ciscoSat = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2))
ciscoDMN = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2))
ciscoDSGUtilities = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5))
ciscoDSGProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 6))
mibBuilder.exportSymbols("CISCO-DMN-DSG-ROOT-MIB", PYSNMP_MODULE_ID=ciscoSPVTG, ciscoDMN=ciscoDMN, ciscoDSGProducts=ciscoDSGProducts, ciscoDSGUtilities=ciscoDSGUtilities, ciscoSPVTG=ciscoSPVTG, ciscoSat=ciscoSat)
