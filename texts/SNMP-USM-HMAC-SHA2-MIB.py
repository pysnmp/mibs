#
# PySNMP MIB module SNMP-USM-HMAC-SHA2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source SNMP-USM-HMAC-SHA2-MIB
# Source digest sha256:5aad4b7e4c9ac201f16d9bbb3541f5a84e2f91d6e7b8231cf6ee047ceb7ddb1f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
snmpAuthProtocols, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "snmpAuthProtocols")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpUsmHmacSha2MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 235))
snmpUsmHmacSha2MIB.setRevisions(('2016-04-18 00:00', '2015-10-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpUsmHmacSha2MIB.setRevisionsDescriptions(('Version correcting the MODULE-IDENTITY value,\n        published as RFC 7860', 'Initial version, published as RFC 7630',))
if mibBuilder.loadTexts: snmpUsmHmacSha2MIB.setLastUpdated('2016-04-18 00:00')
if mibBuilder.loadTexts: snmpUsmHmacSha2MIB.setOrganization('SNMPv3 Working Group')
if mibBuilder.loadTexts: snmpUsmHmacSha2MIB.setContactInfo('WG email: OPSAWG@ietf.org\n                    Subscribe:\n                        https://www.ietf.org/mailman/listinfo/opsawg\n                    Editor:    Johannes Merkle\n                               secunet Security Networks\n                    Postal:    Mergenthaler Allee 77\n                               D-65760 Eschborn\n                               Germany\n                    Phone:     +49 20154543091\n                    Email:     johannes.merkle@secunet.com\n\n                    Co-Editor: Manfred Lochter\n                               Bundesamt fuer Sicherheit in der\n                               Informationstechnik (BSI)\n                    Postal:    Postfach 200363\n                               D-53133 Bonn\n                               Germany\n                    Phone:     +49 228 9582 5643\n                    Email:     manfred.lochter@bsi.bund.de')
if mibBuilder.loadTexts: snmpUsmHmacSha2MIB.setDescription("Definitions of Object Identities needed for the use of\n        HMAC-SHA2 Authentication Protocols by SNMP's User-based Security\n        Model.\n\n        Copyright (c) 2016 IETF Trust and the persons identified as\n        authors of the code.  All rights reserved.\n\n        Redistribution and use in source and binary forms, with or\n        without modification, is permitted pursuant to, and subject\n        to the license terms contained in, the Simplified BSD License\n        set forth in Section 4.c of the IETF Trust's Legal Provisions\n        Relating to IETF Documents\n        (http://trustee.ietf.org/license-info).")
usmHMAC128SHA224AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 4))
if mibBuilder.loadTexts: usmHMAC128SHA224AuthProtocol.setStatus('current')
if mibBuilder.loadTexts: usmHMAC128SHA224AuthProtocol.setDescription('The Authentication Protocol\n                usmHMAC128SHA224AuthProtocol uses HMAC-SHA-224 and\n                truncates output to 128 bits.')
if mibBuilder.loadTexts: usmHMAC128SHA224AuthProtocol.setReference('- Krawczyk, H., Bellare, M., and R. Canetti,\n                HMAC: Keyed-Hashing for Message Authentication,\n                RFC 2104.\n                - National Institute of Standards and Technology,\n                Secure Hash Standard (SHS), FIPS PUB 180-4, 2012.')
usmHMAC192SHA256AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 5))
if mibBuilder.loadTexts: usmHMAC192SHA256AuthProtocol.setStatus('current')
if mibBuilder.loadTexts: usmHMAC192SHA256AuthProtocol.setDescription('The Authentication Protocol\n                usmHMAC192SHA256AuthProtocol uses HMAC-SHA-256 and\n                truncates output to 192 bits.')
if mibBuilder.loadTexts: usmHMAC192SHA256AuthProtocol.setReference('- Krawczyk, H., Bellare, M., and R. Canetti,\n                HMAC: Keyed-Hashing for Message Authentication,\n                RFC 2104.\n                - National Institute of Standards and Technology,\n                Secure Hash Standard (SHS), FIPS PUB 180-4, 2012.')
usmHMAC256SHA384AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 6))
if mibBuilder.loadTexts: usmHMAC256SHA384AuthProtocol.setStatus('current')
if mibBuilder.loadTexts: usmHMAC256SHA384AuthProtocol.setDescription('The Authentication Protocol\n                usmHMAC256SHA384AuthProtocol uses HMAC-SHA-384 and\n                truncates output to 256 bits.')
if mibBuilder.loadTexts: usmHMAC256SHA384AuthProtocol.setReference('- Krawczyk, H., Bellare, M., and R. Canetti,\n                HMAC: Keyed-Hashing for Message Authentication,\n                RFC 2104.\n                - National Institute of Standards and Technology,\n                Secure Hash Standard (SHS), FIPS PUB 180-4, 2012.')
usmHMAC384SHA512AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 7))
if mibBuilder.loadTexts: usmHMAC384SHA512AuthProtocol.setStatus('current')
if mibBuilder.loadTexts: usmHMAC384SHA512AuthProtocol.setDescription('The Authentication Protocol\n                usmHMAC384SHA512AuthProtocol uses HMAC-SHA-512 and\n                truncates output to 384 bits.')
if mibBuilder.loadTexts: usmHMAC384SHA512AuthProtocol.setReference('- Krawczyk, H., Bellare, M., and R. Canetti,\n                HMAC: Keyed-Hashing for Message Authentication,\n                RFC 2104.\n                - National Institute of Standards and Technology,\n                Secure Hash Standard (SHS), FIPS PUB 180-4, 2012.')
mibBuilder.exportSymbols("SNMP-USM-HMAC-SHA2-MIB", PYSNMP_MODULE_ID=snmpUsmHmacSha2MIB, snmpUsmHmacSha2MIB=snmpUsmHmacSha2MIB, usmHMAC128SHA224AuthProtocol=usmHMAC128SHA224AuthProtocol, usmHMAC192SHA256AuthProtocol=usmHMAC192SHA256AuthProtocol, usmHMAC256SHA384AuthProtocol=usmHMAC256SHA384AuthProtocol, usmHMAC384SHA512AuthProtocol=usmHMAC384SHA512AuthProtocol)
